public class Pet {

    private String type;
    private Person owner;

    public Pet(String type, Person owner) {
        this.type = type;
        this.owner = owner;
    }

    public String getType() {
        return type;
    }

    public Person getOwner() {
        return owner;
    }
}