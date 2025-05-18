import queue_ as q
import time
import threading

orders = {'0011':'pizza',
          '0012':'samosa',
          '0013':'pasta',
          '0014':'biryani',
          '0015':'burger',
          '0016':'burger',
          '0017':'pasta'}

OrderQueue = q.Queue()

def orderInsert(orders, OrderQueue):
    for k in orders:
        time.sleep(0.5)
        print(f'New Order Received: {k}| {orders[k]} ')
        OrderQueue.EnqueueDict(k,orders[k])
    OrderQueue.enqueue(None)


def orderpop(OrderQueue):
        while True:
            item = OrderQueue.buffer[-1]
            if item is None:
                 break
            print(f'Order Executed: {OrderQueue.dequeue()}')
            time.sleep(3)

thread1 = threading.Thread(target=orderInsert, args=(orders, OrderQueue))
thread2 = threading.Thread(target=orderpop, args=(OrderQueue,))

thread1.start()
time.sleep(1)
thread2.start()



