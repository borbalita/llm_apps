from celery import shared_task

from app.chat.indexers.pdf_indexer import PDFIndexer
from app.web.db.models import Pdf
from app.web.files import download

pdf_indexer = PDFIndexer()


@shared_task()
def process_document(pdf_id: int):
    pdf = Pdf.find_by(id=pdf_id)
    with download(pdf.id) as pdf_path:
        pdf_indexer(pdf.id, pdf_path)
