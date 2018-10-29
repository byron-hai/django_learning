# -*- coding: utf-8 -*-
from django.db import models


class Model(models.Model):
    model = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name_plural = "Product Models"


class OPN(models.Model):
    opn = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.opn

    class Meta:
        verbose_name_plural = "Product OPNs"


class SN(models.Model):
    serial_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name_plural = "Product Serial Numbers"


class Product(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    serial_number = models.ForeignKey(SN, on_delete=models.CASCADE)
    opn = models.ForeignKey(OPN, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.serial_number, self.opn)

    class Meta:
        verbose_name_plural = "Products"
