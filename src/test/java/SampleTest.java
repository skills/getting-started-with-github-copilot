//import org.junit.BeforeClass;

// import org.testng.annotations.Parameters;
//import org.junit.BeforeClass;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.*;
import org.testng.Assert;
import io.github.bonigarcia.wdm.WebDriverManager;

public class SampleTest {

    WebDriver driver;
    // String browser;
    String a, b;

    @BeforeTest
    public void openBrowser() {
        WebDriverManager.chromedriver();
        driver = new ChromeDriver();
        driver.get("https://www.saucedemo.com/");
        driver.manage().window().maximize();
        this.driver.findElement(By.id("user-name")).sendKeys("standard_user");
        this.driver.findElement(By.id("password")).sendKeys("secret_sauce");
        this.driver.findElement(By.id("login-button")).click();

    }

    @Test(priority = 1)

    public void login() {
        try{
        // this.driver.findElement(By.id("user-name")).sendKeys("standard_user");
        // this.driver.findElement(By.id("password")).sendKeys("secret_sauce");
        // this.driver.findElement(By.id("login-button")).click();
        String actual = driver.getTitle();
        String expected = "Swag Labs";
        Assert.assertEquals(actual, expected);
        System.out.println("Login Successful");
      
        }
        catch(Exception e){
            System.out.println(e);

        }
        //this.driver.close();
    }

    @Test(priority = 2)
    public void invalidTitle() {
        try{
        // this.driver.findElement(By.id("user-name")).sendKeys("standard_user");
        // this.driver.findElement(By.id("password")).sendKeys("secret_sauce");
        // this.driver.findElement(By.id("login-button")).click();
        String actual = driver.getTitle();
        String expected = "Shopping cart";
        System.out.println("Actual Titla is:" + actual);
        Assert.assertNotEquals(actual, expected, "The title doesnot match");
      
        }
        catch(Exception e) {
            System.err.println(e);
        }
        //this.driver.close();
    }

@Test (priority = 3)
    public void testWebElements(){

        // String pageSource = driver.getPageSource();
        // System.out.println(pageSource);
        try {
        List <WebElement> elements =   this.driver.findElements(By.className("inventory_item_label"));/*react-burger-menu-btn */
        System.out.println("Number of elements :" +elements.size());
        System.out.println("index of the elements:" +elements.get(0));

// for(int i=0; i<elements.size();i++){
//     System.out.println("WebElement Text: " +elements.get(i).getAttribute("value"));
// }
        }
        catch (Exception e){}
this.driver.close();
    }

}
