from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es = Elasticsearch(['http://localhost:9200'])

def search_images(query):
    body = {
        'query': {
            'match': {
                'tags': query
            }
        }
    }
    response = es.search(index='images', body=body)
    return response['hits']['hits']

if __name__ == '__main__':
    query = 'nature'
    results = search_images(query)
    for result in results:
        print(result)
