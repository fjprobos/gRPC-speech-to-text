import grpc
from concurrent import futures
import time
import logging
import math

#import classes
import textSender_pb2
import textSender_pb2_grpc


def calculator(number):
    return math.sqrt(number)


def invert(word):
    return word[::-1]


class CalculatorServicer(textSender_pb2_grpc.calculatorServicer):
    def SquareRoot(self, request, context):
        # Create the object that will hold the response
        response = textSender_pb2.Number()
        # Load the response
        response.value = calculator(request.value)
        # Return the response
        return response


class WordInvererServicer(textSender_pb2_grpc.wordInverterServicer):
    def Invert(self, request, context):
        # Create the object that will hold the response
        response = textSender_pb2.Word()
        # Load the response
        response.value = invert(request.value)
        # Return the response
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    textSender_pb2_grpc.add_calculatorServicer_to_server(CalculatorServicer(), server)
    textSender_pb2_grpc.add_wordInverterServicer_to_server(WordInvererServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    logging.log(999, msg="Starting grpc server...")
    serve()
