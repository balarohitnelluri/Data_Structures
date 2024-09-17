class Array():
    def __init__(self) -> None:
        pass


class Static_Array(Array):
        
    def __init__(self) -> None:
            self.static_array=[] 
            self.pointer=0
            #super.__init__(Arrays)
    def static_create(self,size:int,datatype) -> list:
        self.size=size
        self.datatype=datatype.lower()
        try:
            if self.size<=0:
                    raise ValueError("Minimum size atleast 1 ")
            if self.datatype==int or self.datatype not in ['int','char']:
                    raise ValueError("Only enter 'int' for Integers, 'char' for Characters")
        except ValueError as size_error:
            print(size_error)
        except ValueError as datatype_error:
            print(datatype_error)
            
        else:          
            if self.datatype=='int' :
                    self.static_array=[-1]*self.size                     

    def static_insertion(self,value,index=None):
          self.index=index
          self.value=value
          
          if self.index==None:
                    if (self.pointer==self.size):
                        self.static_array[self.pointer-1]=self.value
                    else:
                        self.static_array[self.pointer]=self.value
                        self.pointer+=1                        
          else:
                    try:
                          if self.index>self.size-1 or self.index<0 or self.index>self.pointer-1:
                                raise ValueError(f"Invalid Index! {self.index} is not available current array {self.static_array}")
                    except ValueError as index_error:
                          print(index_error)
                    else:
                        if self.static_array[self.index]==-1:
                            self.static_array[self.index]=self.value
                            self.pointer+=1
                        else:
                            if self.pointer-1!=-1 and self.pointer-1==self.index:
                                  self.static_array[self.index]=self.value
                            
                            else: 
                                counter=self.pointer-1
                                while True:
                                       self.static_array[counter]=self.static_array[counter-1]
                                       counter-=1
                                       if counter==self.index:
                                              self.static_array[counter]=self.value
                                              break
                                       
    def static_deletion(self,index=None):
          self.index=index

          if self.index==None:
                self.static_array[-1]=-1
                self.pointer-=1
          else:
                try:
                          if self.index>self.size-1 or self.index<0 or self.index>self.pointer-1:
                                raise ValueError(f"Exception! Index:{self.index} you are tying to delete is not available curent array size {self.pointer}")
                except ValueError as index_error:
                          print(index_error)
                else:
                            self.static_array[self.index]=-1
                            self.pointer-=1
                            while self.index<self.size-1:
                                self.static_array[self.index]=self.static_array[self.index+1]
                                self.index+=1
                                if self.index==self.size-1:
                                        self.static_array[self.index]=-1
                                        break
                            return self.static_array
                      
    def static_read(self,index=None):
          self.index=index
          if self.index==None:
                print(self.static_array[:self.pointer])
          else:
                try:
                          if self.index>self.size-1 or self.pointer-self.index<0:
                                raise ValueError("Please check the index you've entered")
                except ValueError as index_error:
                          print(index_error)
                else: 
                       if self.index<0 and self.index>=self.pointer:
                             self.index=self.pointer-self.index
                             print(self.static_array[self.index])
                             
                       try:
                              
                            if self.static_array[self.index]==-1:
                                 raise ValueError("Index Location is empty")
                       except ValueError as empty_index:
                             print(empty_index)
                       else:  
                            print(self.static_array[self.index])
          
    def static_update(self,index:int,value:int):
          self.index=index
          self.value=value
          try:
                    if self.index>self.size-1 or self.index<0 and self.index>self.pointer-1:
                                raise ValueError(f"Please check the index again aurrent array size {self.size}")
          except ValueError as index_error:
                          print(index_error)
          else:  
                 self.static_array[self.index]=value
    def check_static_array(self):
           if self.pointer==0:
                 print(self.static_array[:self.pointer])
           else:
                 print(self.static_array[:self.pointer])


#Dynamic Array


class Dynamic_Array(Array):
       def __init__(self) -> None:
              super().__init__()
              self.dynamic_pointer=0
              self.size=0
              self.dynamic_arra=[]
              
       def dynamic_create(self,size:int):
            self.size=size
            self.array=[]
            try:
                if self.size<=0:
                        raise ValueError("Minimum size atleast 1 ")
               
            except ValueError as size_error:
                print(size_error)
                
            else:          
                self.dynamic_array=[-1]*self.size 
                        

       def resize(self):
              newsize=self.size*2
              self.new_rezise_array=[-1]*newsize
                          
              for temp_index in range(self.size):
                     self.new_rezise_array[temp_index]=self.dynamic_array[temp_index]
              self.dynamic_array=self.new_rezise_array
              self.size=len(self.dynamic_array)
              #print(newsize)
              return self.dynamic_array,self.size
       
       def dynamic_shrink(self):
             self.array_shrink=[]
             self.shrink_array_size=0
             print(self.dynamic_pointer,self.size,(self.dynamic_pointer/self.size)*100)
             if (self.dynamic_pointer/self.size)*100<35.0:
                   print("Array Shrinking")
                   self.array_shrink=self.dynamic_array[:self.size//2]
                   self.dynamic_array=self.array_shrink
                   self.size=self.size//2
                   print(self.dynamic_pointer,self.size//2)
             else:
                   return       
       
       def dynamic_insertion(self,value,index=None):
          self.index=index
          self.value=value
          #print(self.size)

          if self.index==None:
                try:
                      if self.dynamic_pointer==self.size:
                        raise ValueError("Arrays is full resizing array......")
        
                except ValueError as resizing_trigger:
                    print(resizing_trigger)
                    self.resize()

                self.dynamic_array[self.dynamic_pointer]=self.value
                self.dynamic_pointer+=1
          else:        
                try:
                    if self.index>self.dynamic_pointer-1 or self.index<0 :
                        raise ValueError("Please check the index you've entered")
                except ValueError as index_error:
                    print(index_error)
                else:
                    if self.dynamic_array[self.index]==self.dynamic_pointer-1:
                        self.dynamic_array[self.index]=self.value
                    else:
                        try:
                                if self.dynamic_pointer==self.size:
                                 raise ValueError("Arrays is full resizing array......")
        
                        except ValueError as resizing_trigger:
                              print(resizing_trigger)
                              self.resize()
                        finally:
                            counter=self.dynamic_pointer       
                           # #(1,2) [1,2,3,4,5,6,-1,-1,-1,-1,-1,-1]   p =6                
                            while True:
                                   #print(self.dynamic_array)
                                   self.dynamic_array[counter]=self.dynamic_array[counter-1]
                                   counter-=1
                                   if self.index==counter:
                                         self.dynamic_array[self.index]=self.value
                                         self.dynamic_pointer+=1
                                         break
       
       def dynamic_deletion(self,index=None):
          self.index=index

          if self.index==None:
                self.dynamic_array[-1]=-1
                self.dynamic_pointer-=1
          else:
                try:
                          if self.index>self.size-1 or self.index<0 or self.index>self.dynamic_pointer-1:
                                raise ValueError(f"Exception! Index:{self.index} you are tying to delete is not available curent array size {self.pointer}")
                except ValueError as index_error:
                          print(index_error)
                else:
                            self.dynamic_array[self.index]=-1
                            self.dynamic_pointer-=1
                            while self.index<self.size-1:
                                self.dynamic_array[self.index]=self.dynamic_array[self.index+1]
                                self.index+=1
                                if self.index==self.size-1:
                                        self.dynamic_array[self.index]=-1
                                        break
          return self.dynamic_shrink()
       
       def dynamic_read(self,index=None):
            self.index=index
            if self.index==None:
                    print(self.dynamic_array[:self.dynamic_pointer])
            else:
                    try:
                            if self.index>self.size-1:
                                    raise IndexError("Please check the index you've entered")
                            if self.index<0:
                                  raise ValueError
                    except IndexError as index_error:
                            print(index_error)
                    except ValueError as negative_index:
                          self.index=self.dynamic_pointer+self.index
                          
                    finally: 
                        try:
                                if self.dynamic_array[self.index]==-1 or self.index<0:
                                    raise ValueError("check index location!")
                        except ValueError as empty_index:
                                print(empty_index)
                        else:  
                                print(self.dynamic_array[self.index])
                
                      
       def check_dynamic_array(self):
            print(self.dynamic_array[:self.dynamic_pointer],self.dynamic_pointer,self.size)

