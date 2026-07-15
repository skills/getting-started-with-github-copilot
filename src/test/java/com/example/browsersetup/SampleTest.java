package com.example.browsersetup;
//import org.junit.BeforeClass;

// import org.testng.annotations.Parameters;
//import org.junit.BeforeClass;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.testng.annotations.*;

import io.github.bonigarcia.wdm.WebDriverManager;

import org.testng.Assert;

public class SampleTest {
    WebDriver driver;

    @BeforeTest
    public  void openBrowser() {
        WebDriverManager.chromedriver().setup();
        driver.manage().window().maximize();
        driver.manage().window().maximize();
        driver.get("https://www.saucedemo.com/");
        driver.findElement(By.id("user-name")).sendKeys("standard_user");
        driver.findElement(By.id("password")).sendKeys("secret_sauce");
        driver.findElement(By.id("login-button")).click();
//return (driver);
    }

    @Test(priority = 1)

    public void login() {
        this.driver.findElement(By.id("user-name")).sendKeys("standard_user");
        this.driver.findElement(By.id("password")).sendKeys("secret_sauce");
        this.driver.findElement(By.id("login-button")).click();
        String actual = driver.getTitle();
        String expected = "Swag Labs";
        Assert.assertEquals(actual, expected);
        System.out.println("Login Successful");
        this.driver.close();
    }

    @Test(priority = 2)
    public void invalidTitle() {
        this.driver.findElement(By.id("user-name")).sendKeys("standard_user");
        this.driver.findElement(By.id("password")).sendKeys("secret_sauce");
        this.driver.findElement(By.id("login-button")).click();
        String actual = driver.getTitle();
        String expected = "Shopping cart";
        System.out.println("Actual Titla is:" + actual);
        Assert.assertNotEquals(actual, expected, "The title doesnot match");
        this.driver.close();
    }

@Test
    public void testWebElements(){

        // String pageSource = driver.getPageSource();
        // System.out.println(pageSource);
        List <WebElement> elements =   this.driver.findElements(By.className("inventory_item_label"));/*react-burger-menu-btn */
        System.out.println("Number of elements :" +elements.size());
        System.out.println("index of the elements:" +elements.get(0));

// for(int i=0; i<elements.size();i++){
//     System.out.println("WebElement Text: " +elements.get(i).getAttribute("value"));
// }

this.driver.close();
    }

}
