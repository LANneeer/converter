from django.db import models
from converter.utils.paths import document_path

#
# class IPAuth(models.Model):
#     ip = models.CharField(max_length=128)
#
#     def __str__(self):
#         return str(self.ip)
#
#
# class IPDocument(models.Model):
#     ip = models.ForeignKey(IPAuth, on_delete=models.CASCADE)
#     document = models.FileField(upload_to=document_path)
#
#     def __str__(self):
#         return str(self.ip)
#
#
# class ConvertingProcess(models.Model):
#     document = models.ForeignKey(IPDocument, on_delete=models.CASCADE)
#     process = models.SmallIntegerField()
#
#     def __str__(self):
#         return str(self.process)
