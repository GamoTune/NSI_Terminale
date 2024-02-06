public class ComputerPioneer {
    private final String lastName;
    private final String firstName;
    private Device device;

    public ComputerPioneer(String lastName, String firstName, Device device){
        this.lastName = lastName;
        this.firstName = firstName;
        this.device = device;
    }

    public String toString(){
        return (this.firstName+""+this.lastName+"is a pioneer in Computer Science");
    }

    public boolean worksOn(Device device) {
        return this.device.equals(device);
    }
}
