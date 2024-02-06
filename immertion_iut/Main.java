public class Main {
    public static void main(String[] args){
        final Device babbage = new Device("Babbage Analytical Machine", 1837);
        final Device turingEngine = new Device("Turing Engine", 1936);
        final ComputerPioneer adaLovelace = new ComputerPioneer("Lovelace", "Ada", babbage);
        final ComputerPioneer alanTuring = new ComputerPioneer("Turing", "Alan", turingEngine);

        System.out.println(adaLovelace);
        System.out.println(alanTuring);
    }
}