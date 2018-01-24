import inspect

def audit_log(called_function):
    def audit_log_inner(*args, **kwargs):
        if inspect.isclass(called_function):
            print("AUDIT {} called with:".format(called_function.__name__) ,args, kwargs)
            #print("AUDIT:",repr(called_function(*args, **kwargs)))
        else:
            try:
                print("AUDIT function ",called_function.__name__,"called with value",repr(args[1]))
                print("AUDIT repr:",repr(args[0]))
                print("AUDIT type:",type(args[0]))
                #args[0].add_audit_entry(called_function.__name__ + "set to" + repr(args[1]))
            except:
                print("AUDIT: no name")
                pass

        result = called_function(*args, **kwargs)
        return result
    return audit_log_inner

# class audit_log:
#     def __init__(self,function):
#         self.function = function
#         self.audit = []
#         # print("audit init")
#     def __call__(self, *args, **kwargs):
#         if inspect.isclass(self.function):
#             self.audit.append(repr(self.function(*args, **kwargs)))
#         else:
#             try:
#                 self.audit.append(self.function.__name__,"set to",repr(args[1]))
#             except:
#                 pass
#         # print("AUDIT: ",self.audit[-1::])
#         print("FULL AUDIT: ",self.audit)
#         return self.function(*args, **kwargs)
