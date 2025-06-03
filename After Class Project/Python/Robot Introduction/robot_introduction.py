class introElement:
    def __init__(self, robotName, modelNumber, powerSystem, mechanicalHardwareSupplier, function, introductionLine):
        self.robotName = robotName
        self.modelNumber = modelNumber
        self.powerSystem = powerSystem
        self.mechanicalHardwareSupplier = mechanicalHardwareSupplier
        self.function = function
        self.introductionLine = introductionLine

    def introduce(self):
        print('**-------------------------*---------------------------**')
        print(f'{self.introductionLine}')
        print(f'Name: {self.robotName}')
        print(f'Model Number: {self.modelNumber}')
        print(f'Power System: {self.powerSystem}')
        print(f'Mechanical Hardwar Supplier: {self.mechanicalHardwareSupplier}')
        print(f'Function: {self.function}')  
        print('**-------------------------*---------------------------**')


    
robot1 = introElement(
    robotName="Astra",
    modelNumber="AX-2025",
    powerSystem="Fusion Core",
    mechanicalHardwareSupplier="NanoTech Industries",
    function="Interstellar Exploration",
    introductionLine="Greetings, Earthlings. I am Astra, your cosmic companion!"
)

robot2 = introElement(
    robotName="Bolt",
    modelNumber="BZ-99",
    powerSystem="Solar Cells",
    mechanicalHardwareSupplier="SunWorks Robotics",
    function="Disaster Response",
    introductionLine="Hello! I am Bolt, here to rescue and assist in emergencies!"
)

robot1.introduce()
robot2.introduce()
