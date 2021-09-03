import pdb

from bs4 import BeautifulSoup

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from core.repositories import ScraperRepository

from urllib import parse
import requests


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_submission(request):
    try:
        if parse.urlparse(request.data['url']).hostname == 'fabelio':
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
            page = requests.get(request.data['url'], headers=header)
            soup = BeautifulSoup(page.content, 'html.parser')

            name = soup.find(id='product-name').get_text()
            price = soup.find(id="product-final-price").get_text()
            url = request.data['url']
            description = soup.find_all('span', {'class': 's1'}) if soup.find_all('span', {'class': 's1'}) else soup.find_all('em')
            image = soup.find(id='product-image').get('src')

            data = {
                'name': name,
                'price': price,
                'url': url,
                'description': description,
                'image': image
            }
            scraper = ScraperRepository.create(data)
            return Response(
                data={'id': scraper},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={'message': 'Input fabelio url'},
                status=status.HTTP_400_BAD_REQUEST)
    except Exception as exp:
        return Response(
            data={'message': 'Internal server error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_submission(request):
    data = ScraperRepository.read()
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_submission_by_id(request, id):
    data = ScraperRepository.read_by_id(id)
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )
