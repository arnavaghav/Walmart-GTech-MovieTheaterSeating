# Walmart-GTech-MovieTheaterSeating --- Arnav Aghav

This project is my answer using Python programming language for the back-end variant of the Walmart Pre-interview assessment.  Test cases have been developed for this project. The assumptions Specification of test cases Can be found below. 

Note: This project reqires Python3+ to run.

## Approach
- Based on the requirement, we want to always maintain a 3 seat and/or row buffer. Therefore, initially we allocate as many seats as we can in a consecutive. Then if we reach EOF and have remaining empty rows, we can move groups from rows with multiple other groups to the following spaces. This way, maximum no. of customers can be seated first before we reach EOF. 
- Rservation of more than 20 people, will be split until we get groups with sizes <= 20
- Output will be calculated after EOF or capacity reached. 
- ✨Magic ✨

## Assumptions
- The requirement of 3 seat buffer is absolute but the requirement for one row buffer is optional based on if capacity is available. 
- When there is no more seating left, the program exits not parsing any further reservations.
- Edge cases: When there is seating available but not in a consecutive manner for a group to sit together, the program won't allocate any seats to the reservation request. If required, functionality can be added to split up the groups and seat them.
- We assume that most comfortable rows start from J and onwards to the screen, and therefore allocate seats accordingly.

## Testing

For this project, we've developed a couple of test cases.  For future work, we can automate the testing by building a pytest suite for the same. We can also do intergration testing with the desired enviroment we want to integrate it with. Current testing is functional in nature. Further blackbox testing can be achieved by doing equivalent-partitioning, CFG/static analysis, and fuzz testing for a robust program.  
