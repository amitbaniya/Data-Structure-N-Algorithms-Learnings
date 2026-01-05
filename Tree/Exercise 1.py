class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level


    def print_tree(self, data):
        spaces = ' ' * self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        if data == 'name':
            print(prefix + self.name)
        elif data == 'designation':
            print(prefix + self.designation)
        else:
            print(prefix + self.name + '(' + self.designation + ')')

        if self.children:
            for child in self.children:
                child.print_tree(data)



def build_tree():
    CEO = TreeNode("Nilupur", "CEO")
    CTO = TreeNode("Chinmey", "CTO")
    HRHead = TreeNode("Gels","HR Head")

    InfrastructureHead = TreeNode("Vishwa", "Infrastructure Head")

    InfrastructureHead.add_child(TreeNode("Dhaval", "Cloud Manager"))
    InfrastructureHead.add_child(TreeNode("Abhijit", "App Manager"))

    CTO.add_child(InfrastructureHead)

    HRHead.add_child(TreeNode("Peter", "Recruitment Manager"))
    HRHead.add_child(TreeNode("Waqas", "Policy Manager"))

    CEO.add_child(CTO)
    CEO.add_child(HRHead)

    print(CEO.print_tree("designation"))

if __name__ == '__main__':
    build_tree()
