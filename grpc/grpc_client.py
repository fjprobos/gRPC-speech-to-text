import grpc
from concurrent import futures
import time
import pandas as pd

# Import classes
import textSender_pb2
import textSender_pb2_grpc

# Open a GRPC channel
channel = grpc.insecure_channel('54.209.72.104:50051')

# Create the stub from the compiled pb2 file
wordStub = textSender_pb2_grpc.wordInverterStub(channel)

# Create a valid request message (see proto file)
word = textSender_pb2.Word(value="hola")

# Make the call
response = wordStub.Invert(word)


number = textSender_pb2.Number(value=16)
text = "Go bid thy mistress, when my drink is ready, She strike upon the bell. Get thee to bed. Servant exits. Is this a dagger which I see before me, The handle toward my hand? Come, let me clutch thee. I have thee not, and yet I see thee still. Art thou not, fatal vision, sensible To feeling as to sight? Or art thou but A dagger of the mind, a false creation Proceeding from the heat-oppressèd brain? I see thee yet, in form as palpable As this which now I draw.He draws his dagger. Thou marshal’st me the way that I was going, And such an instrument I was to use. Mine eyes are made the fools o’ th’ other senses Or else worth all the rest. I see thee still, And, on thy blade and dudgeon, gouts of blood, Which was not so before. There’s no such thing. It is the bloody business which informs Thus to mine eyes. Now o’er the one-half world Nature seems dead, and wicked dreams abuse The curtained sleep. Witchcraft celebrates Pale Hecate’s off’rings, and withered murder, Alarumed by his sentinel, the wolf, Whose howl’s his watch, thus with his stealthy pace, With Tarquin’s ravishing strides, towards his design Moves like a ghost. Thou sure and firm-set earth, Hear not my steps, which way they walk, for fear Thy very stones prate of my whereabouts And take the present horror from the time, Which now suits with it. Whiles I threat, he lives. Words to the heat of deeds too cold breath gives. A bell rings. I go, and it is done. The bell invites me. Hear it not, Duncan, for it is a knell That summons thee to heaven or to hell."
#text = "la prueba"
starts = []
ends = []
latencies = []
words = []

## Experiment 1
word = textSender_pb2.Word(value=text)
response = wordStub.Invert(word)
init = time.perf_counter_ns()/1000000
response = wordStub.Invert(word)
end = time.perf_counter_ns()/1000000
print(response)
print("init: " + str(init))
print("end: " + str(end))
print(end - init)


## Experiment 2

# for t in text:
#     word = textSender_pb2.Word(value=t)
#     init = time.perf_counter_ns()/1000000
#     # Make the call
#     response = wordStub.Invert(word)
#     end = time.perf_counter_ns()/1000000
#     starts.append(init)
#     ends.append(end)
#     latencies.append(end-init)
#     words.append(t)
#
#     print(response)
#     print("init: " + str(init))
#     print("end: " + str(end))
#
# df = pd.DataFrame(list(zip(words, starts, ends, latencies)), columns=['string', 'start_ms', 'end_ms', 'latency_ms'])
# df.to_csv("latencies.csv")
# print(latencies)
