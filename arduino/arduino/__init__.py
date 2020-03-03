from django.shortcuts import render


def post_list(request):
    n = ["Mambetaliev", "aaa", "ggg", "eee"]
    return render(request, "driver/index.html", context={'name': n})