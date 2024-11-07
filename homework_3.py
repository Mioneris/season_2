class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    @cpu.setter
    def cpu(self,value):
        self.__cpu = value

    @memory.setter
    def memory(self,value):
        self.__memory = value

    def make_computations(self):
      addition = self.cpu + self.memory
      subtraction = self.cpu - self.memory
      multiplication = self.cpu * self.memory
      division = round(self.cpu / self.memory, 2) if self.memory != 0 else 'Деление на 0 невозможно'

      return {"addition":addition,
              'subtraction':subtraction,
              'multiplication':multiplication,
              'division':division
              }

    def __str__(self):
        return f"Computer with {self.__cpu} GHz CPU and {self.__memory} GB memory\n"

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory
    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

# computer_computations = Computer(10,12)
# results = computer_computations.make_computations()
# print(results)
# PC = Computer('Amd Ryzen 5', '12GB')
# print(PC)

class Phone:
    def __init__(self,sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self,value):
        self.__sim_cards_list = value

    def call(self, sim_card_number,call_to_number):
        try:
            print(f'Идет звонок на номер {call_to_number} '
                  f'с сим-карты {sim_card_number} -'
                  f' {self.__sim_cards_list[sim_card_number - 1]}')
        except IndexError:
            print(f'Сим-карта не найдена!Используйте 1-2-3 для выбора сим-карты{self.__sim_cards_list}.')

    def __str__(self):
        return f'\nPHONE SIM-CARDS : {str(self.__sim_cards_list)}\n'


# phone = Phone(['Beeline', 'MegaCom', 'O!'])
#
# print(phone)
#
# phone.call(1, "+996553112433")

class SmartPhone(Computer,Phone):
    def __init__(self,cpu,memory,sim_cards_list):
        Computer.__init__(self,cpu,memory)
        Phone.__init__(self,sim_cards_list)

    def use_gps(self,location):
        return f'Маршрут проложен до локации {location}'

    def __str__(self):
        return f'\nSmartphone INFO:\n' \
               f'CPU : {self.cpu}, MEMORY:{self.memory}\n' \
               f'Sim-Cards: {self.sim_cards_list}\n'

# smartPhone = SmartPhone('M1', '12GB',['Beeline', 'MegaCom', 'O!'])
# print(smartPhone)
""""""
computer = Computer(10, 12)
print(computer)
print(computer.make_computations())

phone = Phone(['Beeline', 'MegaCom', 'O!'])
print(phone)
phone.call(1, "+996553112433")
phone.call(2, "+996553112433")
phone.call(3, "+996553112433")
phone.call(4, "+996553112433")

smartphone1 = SmartPhone('A14', '12GB', ['O!', 'MegaCom'])
smartphone2 = SmartPhone('Qualcomm Snapdragon 8 Gen 3', '12GB',['MegaCom', 'Beeline'])
print(smartphone1)
print(smartphone2)




