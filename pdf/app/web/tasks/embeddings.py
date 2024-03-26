from app.chat.embedding import PDFEmbedder
from app.web.db.models import Pdf
from app.web.files import download
from celery import shared_task

pdf_embedder = PDFEmbedder()


@shared_task()
def process_document(pdf_id: int):
    pdf = Pdf.find_by(id=pdf_id)
    with download(pdf.id) as pdf_path:
        pdf_embedder(pdf.id, pdf_path)
