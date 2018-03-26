import boto3
import base64

with open("test/images/dog.jpg", "rb") as imageFile:
	f = imageFile.read()
	b = bytearray(f)

	client = boto3.client('rekognition')

	response = client.detect_labels(
		Image={
	    	'Bytes': b,
	    },
	    MaxLabels=10
	)
	print(response['Labels'])