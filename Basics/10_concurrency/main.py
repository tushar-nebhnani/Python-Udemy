"""
    Concurrency: 
    Doing multiple things at once.

    Module: threading.Thread, asyncio
    Thread knows their entry points so even if don't mention the main function it will execute by itself.

    Thread shines in i/o operation and web request. They can share memory with each other.

    Ex: Talking to a friend while making chai
"""

""""
    Parallelism: Running many things are exactly same time. 
    In a program, when you run different process at the same time but flaw that you cannot return the result before all the process have been completed and they have returned their values. And plus the time to combine all those results will also be taken into account.

    Module: multiprocession.Process, concurrent.futures.ProcessPoolExecutor
    Multiprocessing doesn't know their entry points so even if we don't mention the main function it will not execute by itself. We have to explicitly mention it.

    # When we do not mention main function this error occurs.
    ERROR: ' 
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ... 
    '
    They do not share memory with each other.
    
    Ex: Two people making chai
"""