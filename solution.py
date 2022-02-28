# Standard imports
import sys

# Declaration of global variables
rows = 10
cols = 20
totalSeats = rows * cols
bufferSeats = 3

class Theater:
    
    # Class vars
    seatMap = []
    allocatedSeats = {}

    # Setup an empty theater
    def __init__(self) -> None:
        for row in range(rows):
            temp = ["#"] * cols
            temp.append(20)
            self.seatMap.append(temp)


    """Possible optimizations: maintain priorityQueue/maxHeap of available seats and their respective rows
                               to quickly check if allocation is possible.
    """
    # This method tries to find and allocates seats given the constraints
    # Params: Reservation ID and the number of requested seats
    # Returns string of either the allocated seat numbers or the message of full capacity 
    def seatGroup(self, reservationID, requestedSeats) -> str:
        
        seatsAvailable = False

        # In a successful allocation, return the allocated seats in the format (e.g R001 A1, A2, A3)
        # Start searching for seats in the upper rows
        for idx, row in enumerate(self.seatMap):
            
            seatsAllocated = ""
            
            # Check available seats 
            availableSeats = row[-1]

            # Flag variable to check if loop ends to determine why seat wasn't allocated.
            if availableSeats > 0:
                seatsAvailable = True

            if availableSeats < requestedSeats:
                pass

            # Can seat group here
            if availableSeats >= requestedSeats:                
                buffers = 0
                bufferSet = False

                for seatNumber, seat in enumerate(row):
                    
                    # Exit condition
                    if bufferSet and requestedSeats == 0:
                        break
                    
                    # Allocate the seat or set it as buffer
                    if seat == "#":

                        # First allocate seat
                        if requestedSeats > 0:
                            seatsAllocated += "{}{} ".format(self.getRowID(idx), seatNumber)
                            row[seatNumber] = reservationID
                            requestedSeats -= 1
                            row[-1] -= 1

                        else:
                            row[seatNumber] = "b"
                            
                            # Deduct count
                            buffers += 1
                            row[-1] -= 1
                            
                            # Check if required buffers are filled
                            if buffers == 3:
                                bufferSet = True
                    
                    # Keep finding empty seat
                    else:
                        continue

                return reservationID + " " + seatsAllocated   

        # If we We want to return a null string to indicate if this group can't be seated in "available" space.
        if seatsAvailable:
            return "Cannot allocate seats to this reservation!"

        # We want to return a capacity reached string to stop parsing further input.
        return "Capacity Reached!"

    # Helper function to get the row ID 
    def getRowID(self, idx):
        charIndex = 9 - idx + 65
        return chr(charIndex)
    
    # Validate the requested seats number
    def validateInput(self, requestedSeats):
        if requestedSeats <= 0:
            return False
        # Cannot allocate more than the theatre capacity 
        if requestedSeats >= 200:
            return False
        return True


    # This method writes the seat reservations to the output file
    # Params: output file descriptor and reservation string
    # Returns none 
    def writeAllocationOutput(self, o, allocationResult):
        try:
            if allocationResult != "":
                o.write(allocationResult + "\n")
        except Exception as e:
            print("Error in writing to output file: {}".format(str(e)))


    # This method parses the input file line by line and passes it to the seatGroup method 
    # for allocating seats if possible.
    # Params: Input and output file descriptors
    # Returns none since it writes to the output file and we've handled exceptions  
    def parseInput(self, f, o):
        try:
            # Every reservation is a new line
            for line in f:
                print(line)
                reservationID = line.split(" ")[0]
                requestedSeats = int(line.split(" ")[1])
                
                # Check if input is valid
                if (self.validateInput(requestedSeats)):
                    allocationResult = self.seatGroup(reservationID, requestedSeats)
                    
                    if allocationResult == "Capacity Reached!":
                        break
                    elif allocationResult == "Cannot allocate seats to this reservation!":
                        print("Cannot allocate seats to this reservation!")
                    else:
                        # Write the returned output
                        self.writeAllocationOutput(o, allocationResult)
                    
        except Exception as eror:
            print("Couldn't find the input file! Error: {}".format(eror))
        except ValueError:
            print("Invalid requested number of seats")
        except Exception as e:
            print("There was an error: {}".format(str(e)))


    def printArrangement(self) -> None:
        for row in self.seatMap:
            print(row)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Please execute the script in the following format:\npython solution.py <input_file>")

    # Allocations
    input_file = sys.argv[1]
    f = ""

    # Try opening given input file
    # Poissible sec vulnerability here but
    try:
        f = open(input_file, "r")
        o = open("ouput.txt", "a")

    except IOError:
        sys.exit("Error: File does not appear to exist.")

    o.write("----Testing {} ----\n".format(input_file))

    # Create our Theater class and seat
    theater = Theater()
    theater.parseInput(f, o)
    theater.printArrangement()
