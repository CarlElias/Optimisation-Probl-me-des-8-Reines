
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Main m = new Main();
        int k = 0;
        ArrayList<String> listeTabou = new ArrayList<String>();
        int[] tableauFinal = m.newRandomTab(8);
        int[] copie = tableauFinal.clone();
        int actualConflit = m.conflit(tableauFinal);
        int aspiration = actualConflit - 1;
        int[][] voisinage = new int[50][8];
        int[] voisinSelectionner = new int[8];
        String footrint = "";
        listeTabou.add(m.arrayToString(tableauFinal));
        while (m.conflit(copie) > 0){
            k++;
            System.out.println("\n\n\n ======================> ETAPE " + k);
            voisinage = m.genererVoisinage(copie);
            voisinSelectionner = m.selectionnerPlusPetitVoisinage(voisinage);
            footrint = m.arrayToString(voisinSelectionner);

            if(listeTabou.contains(footrint)){
                if(!(m.conflit(voisinSelectionner) <= aspiration)){
                    System.out.println("==> CRITERE D'ASPIRATION NON SATISFAIT");
                    System.out.println("==> RECHERCHE DE NOUVEAU MEILLEUR VOISIN");
                    continue;
                }
            }

            aspiration = m.conflit(voisinSelectionner) - 1;
            copie = voisinSelectionner.clone();
            listeTabou.add(footrint);
            System.out.println("======================================>");
        }
        for(String i: listeTabou){
            System.out.println(i);
        }
        m.printTab(copie, "", "");
    }

    public int[][] genererVoisinage(int[] tab){
        printTab(tab, "====> RECHERCHE DES VOISINS DU TABLEAU", "===> VOISINS TROUVES : ");
        int i = 50;
        int positionToModify;
        int[] copie = new int[8];
        int[][] voisinage = new int[50][8];
        while (i > 0){
            copie = tab.clone();
            positionToModify = (int) ((Math.random() * (7)) + 0);
            copie[positionToModify] = (copie[positionToModify] + (int) ((Math.random() * (10000 - 500)) + 500)) % 8;
            if(eviterDuplication(voisinage, copie)){
                continue;
            }
            voisinage[50 - i] = copie.clone();
            printTab(copie.clone(), "", "");
            i--;
        }
        System.out.println("====> FIN DE LA GENERATION DES VOISINS");
        return voisinage;
    }

    public int[] selectionnerPlusPetitVoisinage(int[][] voisinage){
        System.out.println("====> SELECTION DU VOISIN");
        int conflitPrecedent;
        int[] voisinSelectionner = voisinage[0].clone();
        int conflitActuel = conflit(voisinSelectionner);
        for (int i = 1; i< voisinage.length; i++){
            conflitPrecedent = conflit(voisinage[i]);
            if(conflitPrecedent < conflitActuel){
                voisinSelectionner = voisinage[i].clone();
                conflitActuel = conflit(voisinSelectionner);
            }
        }
        printTab(voisinSelectionner, "Le voisin sélectionné est : ", "====> FIN DE LA SELECTION DES VOISINS");
        return voisinSelectionner;
    }

    public int[] newRandomTab(int size){
        int[] tabToReturn = new int[size];
        for(int i = 0; i < size; i++){
            tabToReturn[i] = (int) ((Math.random() * (7 - 0)) + 0);
        }
        return tabToReturn;
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

    public String arrayToString(int[] tab){
        StringBuilder str = new StringBuilder();
        for (int j : tab) {
            str.append(j);
        }
        return str.toString();
    }

    public boolean eviterDuplication(int[][] arrayToCheck, int[] arrayToFind){
        boolean found =  false;
        for (int i = 0; i< arrayToCheck.length; i++){
            for (int j = 0; j < arrayToCheck[i].length; j++){
                if(arrayToCheck[i][j] != arrayToFind[j]){
                    found = false;
                    break;
                }
                found = true;
            }
            if(found){
                break;
            }
        }
        return found;
    }

    public void printTab(int[] tab, String startMessage, String endMessage){
        if(!startMessage.equals("")){
            System.out.println(startMessage);
        }

        System.out.print("(");
        for (int i = 0; i < tab.length; i++){
            System.out.print(tab[i]);
            if(i < tab.length - 1){
                System.out.print(",");
            }
        }
        System.out.println(") -- Conflit = " + conflit(tab));

        if(!endMessage.equals("")){
            System.out.println(endMessage);
        }

    }
}
