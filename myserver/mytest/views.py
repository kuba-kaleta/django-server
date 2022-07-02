from django.shortcuts import render


def mytest(response):
    return render(response, "experiment.html")


def findall(response):
    return render(response, "findall.html")

