from psutil import process_iter, AccessDenied, NoSuchProcess

for proc in process_iter():
    try:
        processName = proc.name()
        processID = proc.pid
        print(f"{processID:<15} {processName}")

    except (NoSuchProcess, AccessDenied):
        pass
