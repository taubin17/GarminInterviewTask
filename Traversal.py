# Program created by Tyler Aubin
# Program finds node labeled "FindMe"
# Program must print out the name of each node traversed
# Program stops searching (Returns)  when "FindMe" is found

class Node:
    # Data is value passed in to node
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Search the tree
    def traverse(self, value):

        # Print each node value traversed as constrained
        print(self.data)

        # Check if the node value is "FindMe". IF so, we're done.
        if self.data == "FindMe":
            print("\nFound it!")
            return True


        # If not a leaf & If node on left side
        if self.left:

            # Traverse left
            res1 = self.left.traverse(value)

            # If "FindMe" was found, return True
            if res1 is True:
                return True

        # If not a leaf & If node on right side
        if self.right:

            # Traverse right
            res2 = self.right.traverse(value)

            # If "FindMe" was found, return True
            if res2 is True:
                return True


def main():
    start = Node("Start")
    start.left = Node("A1")
    start.right = Node("A2")
    start.left.left = Node("D1")
    start.left.left.left = Node("E1")
    start.right.left = Node("B1")
    start.right.right = Node("B2")
    start.right.left.left = Node("FindMe")
    start.right.right.left = Node("C1")

    start.traverse("FindMe")

if __name__ == '__main__':
    main()
    
