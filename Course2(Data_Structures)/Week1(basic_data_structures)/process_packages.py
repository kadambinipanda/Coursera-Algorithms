# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.curr_time = 0
        self.finish = []


    def process(self, request):
        while self.finish and self.finish[0] <= request.arrived_at:
            self.finish.pop(0)

        if len(self.finish) < self.size:
            if self.curr_time <= request.arrived_at:
                self.curr_time = request.arrived_at + request.time_to_process
                self.finish.append(self.curr_time)
            else:
                self.curr_time += request.time_to_process
                self.finish.append(self.curr_time)
            return Response(False, self.finish[-1] - request.time_to_process)
        else:
            return Response(True, -1)



def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
