import subprocess as sp
import shutil

class ProgressLite(self):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        doClear     - Optional  : doClear (Bool)
        isBash      - Optional  : isBash (Bool)
        decimals    - Optional  : number of decimal places in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    def printProgress(self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        twx, twy = shutil.get_terminal_size()
        length = twx - 1 - len(prefix) - len(suffix) - 10
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        if doClear:
            if isBash:
                tmp = sp.call('clear',shell=True)
            else:
                tmp = sp.call('cls',shell=True)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

        # Print New Line on Complete
        if iteration == total: 
            print()
