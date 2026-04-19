public class Main {

    public static void main(String[] args) {

        Person person = new Person("Ana");
        Pet pet = new Pet("Dog", person);

        System.out.println(person.getName() + " owns a " + pet.getType());
    }
}