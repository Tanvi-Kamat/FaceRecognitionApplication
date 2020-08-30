import json
from json import JSONEncoder
import numpy
import facevector_generator

# convert array of points on face into a list
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

# based on whether or not there are 128 points given in parameter
# return a success or failure result in dictionary format, not json format yet
def success_fail(encodingPoints):
    if encodingPoints:
        # success result, has points
        face_vector_dict = {
            'faceVector': encodingPoints,
            'result': 'Success',
            'message': '',
            'errorCode': 0
        }
    else:
        # failure result, no face detected
        face_vector_dict = {
            'faceVector': 'null',
            'result': 'Failure',
            'message': 'Failed to detect face',
            'errorCode': 1
        }
    return face_vector_dict

# get encodings of a file in json format
def get_encodings(photoFile):
    # use function from other python file to get face points from user's image
    encodings_128D = facevector_generator.make_vector(photoFile)
    # store dictionary format result using user's 128D face points
    data_dict = success_fail(encodings_128D)
    # convert dictionary-format list into json-format object
    json_encodings = json.dumps(data_dict, cls=NumpyArrayEncoder, indent=2)
    return json_encodings
