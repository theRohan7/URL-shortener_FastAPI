from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app import schemas, models, utils, config
from app.database import sessionLocal

router = APIRouter()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/shorten')
def create_short_url(request: schemas.URLRequest, db: Session = Depends(get_db)):
    existing_url = db.query(models.Url).filter(models.Url.original_url == str(request.url)).first()

    if existing_url:
        short_url = f"{config.settings.BASE_URL}/{existing_url.short_url}"
        return {"short_url": short_url}
    
    short_link = utils.generate_short_link()
    while db.query(models.Url).filter(models.Url.short_url == short_link).first():
        short_link = utils.generate_short_link()

    
    new_url = models.Url(original_url = str(request.url), short_url = short_link)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    short_url = f"{config.settings.BASE_URL}/{new_url.short_url}"
    return {"short_url": short_url}

@router.get('/{short_link}')
def redirect_to_url(short_link: str, db: Session = Depends(get_db)):

    url = db.query(models.Url).filter(models.Url.short_url == str(short_link)).first()
    
    if not url: 
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url=url.original_url)