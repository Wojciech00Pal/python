/*LAB2. Design of a data center*/

include <stdio.h>
include <stdlib.h>
include <math.h>

int main(int argc, char *argv[])
{
    float overSubs = 0; 
    int swtTor = 0;
    int swtSpine = 0;
    
    char* nServers = argv[1];
    char* nPortX = argv[2];
    char* nPortY = argv[3];
    
    if(argc != 4) {
        printf("You must enter 2 numbers!");
        exit(0);
    }else{
        int nSs = atoi(nServers);
        int nPX = atoi(nPortX);
        int nPY = atoi(nPortY);
        
        overSubs = nPX/nPY;
        swtTor = ceil(nSs/nPX);
        swtSpine = nPY;
        
        printf("\n#Tor switches = %d\n#Spine switches = %d\nOversubscription = %0.2f", swtTor, swtSpine, overSubs);
        
    }

}
