import urllib.request as ur
import flags
import os
import time
import multiprocessing as mp

def getGifs():
    if not os.path.exists('flags'):
        os.makedirs('flags')
    url = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
    for item in flags.flags:
        name = item + '-lgflag.gif'
        ur.urlretrieve(url + name, 'flags/' + name)
    ur.urlcleanup()

def main():
    print('Starting process...')
    start = time.time()
    cpu = time.process_time()

    procs = []
    for n in range(4):
        proc = mp.Process(target=getGifs)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    end = time.time()-start
    cpuEnd = time.process_time()-cpu

    with open('fprocess.txt', 'w') as f:
        f.write(str(os.path.getsize('flags')) + ' bytes downloaded\n')
        f.write('It took ' + str(end) + ' seconds\n')
        f.write('It took the CPU ' + str(cpuEnd) + ' seconds\n')
    print('Finished')

if __name__ == "__main__":
    main()