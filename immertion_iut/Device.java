public class Device {
    private final String name;
    private final Integer inventionYear;

    public Device(String name, Integer inventionYear){
        this.name = name;
        this.inventionYear = inventionYear;
    }

    public String getName(){
        return this.name;
    }

    public Integer getYear(){
        return this.inventionYear;
    }

    public String toString(){
        return "The "+this.name+" was invented in "+this.inventionYear+".";
    }
}