console.log(localStorage.getItem("acntno"));
class Bank {

    static accountDetails() {
        let userData = {
            1000: { acno: 1000, pswd: "userone", balance: 5000 },
            1001: { acno: 1001, pswd: "usertwo", balance: 5000 },
            1002: { acno: 1002, pswd: "userthree", balance: 5000 },
        }
        return userData

    }

    static authenticate(acno, pswd) {
        var dataset = Bank.accountDetails()
        if (acno in dataset) {
            if (pswd == dataset[acno]["pswd"]) {
                return 1
                // alert("fdhhgf")
                //sucessfull authentication

            }
            else {
                ///invalid password
                return 0
            }
        }
        else {
            //invalid accno
            return -1
        }
    }
    static setStorage(acntno, pswd) {
        //letStorage.setItem("acntno",acntno)
        //letStorage.setItem("pswd",pswd)
        let obj = {
            actno: acntno,
            pswd: pswd//objectine store cheyyan
        }
        localStorage.setItem("data", JSON.stringify(obj))
    }

    static login() {
        var acno = document.querySelector("#acno").value
        var pswd = document.querySelector("#pwd").value

        let user = Bank.authenticate(acno, pswd)//0 1 -1
        if (user == 0) {
            alert("invalid password")
        }
        else if (user == 1) {
            alert("sucess")
            window.location.href = "home.html"
        }
        else if (user == -1) {
            alert("invalid account number")
        }

    }
    withdrawal() {

    }
    deposit() {

    }
}