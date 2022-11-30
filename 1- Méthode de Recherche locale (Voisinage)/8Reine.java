package com.azkam;
 
public class Main {
 
    public static void main(String[] args) {
        Main m = new Main();
        int[] vals = {1,1,1,1,1,1,1,1};
        for(int i =0; i < vals.length; i++){
            vals[i] = (int) ((Math.random() * (8 - 1)) + 1);
        }
        int counter = 0;
        int[] tempVal = new int[8];
        int[] tempVal2 = new int[8];
        tempVal = vals;
        int positionToModify;
        int actualConf = m.conflit(vals);
        int prevAcutalConf = 0;
        while(true){
            for (int i = 0; i < 20; i++) {
                positionToModify = (int) ((Math.random() * (7)) + 0);
                tempVal[positionToModify] = (tempVal[positionToModify] + 1 ) % 8;
 
                if(actualConf > m.conflit(tempVal)){
                    for(int j = 0; j < tempVal.length; j++){
                        System.out.print(tempVal[j] + ",");
                    }
                    System.out.println(" | " + m.conflit(tempVal));
                    actualConf = m.conflit(tempVal);
                    for(int k = 0; k < tempVal.length; k++){
                        tempVal2[k] = tempVal[k];
                    }
                }
                tempVal = vals;
            }
            for(int k = 0; k < tempVal.length; k++){
                tempVal[k] = tempVal2[k];
                vals[k] = tempVal2[k];
            }
            if(actualConf == prevAcutalConf){
                counter++;
            }
            if(counter == 15000){
                break;
            }
            prevAcutalConf = actualConf;
        }
 
    }
 
 
 
    public int conflit(int[] tab){
        int conflits = 0;
        for(int i  = 0; i < tab.length; i++ ){
            for(int j = 0; j < tab.length; j++){
                conflits += (tab[i] == tab[j]) && (i!=j) ? 1 : 0;
                conflits += (Math.abs(tab[i] - tab[j]) == Math.abs(i - j)) && (i!=j) ? 1 : 0;
            }
        }
        return conflits;
    }
 
 
}
 