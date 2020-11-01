from google.cloud import vision
import io

client = vision.ImageAnnotatorClient()

with io.open('/home/reciet_curry.jpg', 'rb') as image_file:
    
    content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))