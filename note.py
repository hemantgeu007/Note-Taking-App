class Note:
    #method of initializing a note
    def __init__(self,idt=0,msg="",time=""):
        self.__idt=idt
        self.__msg=msg
        self.__time=time

    #method to get a note
    def get_msg(self):
        return self.__msg

    #method to get id
    def get_idt(self):
        return self.__idt

    #method to get time
    def get_time(self):
        return self.__time

    # method to set a note
    def set_msg(self,msg):
        self.__msg=msg

    # method to set id
    def set_idt(self,idt):
        self.__idt=idt

    # method to set time
    def set_time(self,time):
        self.__time=time