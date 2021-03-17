class Bank {

    static accountDetails() {
        let userdata = {
            1000: { accno: 1000, password: "user1", balance: 5000 },
            1001: { accno: 1001, password: "user2", balance: 1000 },
            1002: { accno: 1002, password: "user3", balance: 3000 },


        }
        return userdata
    }
    static authenticate(accno, password) {
      alert(password)
        var dataset = Bank.accountDetails()
        if (accno in dataset) {
            if (password == dataset[accno]['password']) {
                
                return 1
                //succesfull authentication
            }

            else {
                return 0
                //invalid password
            }
        }
        else {
            return -1 //invalid accno
        }
    }
    static login() {
        var accno = document.querySelector("#accno").value
        var password = document.querySelector("#pwd").value
        let user = Bank.authenticate(accno, password)
        
        if (user == 0) {
            alert("invalid password")

        }
        else if (user == 1) {
            alert("succes")
            window.location.href="home.html"
            
            
        }
        else if (user == -1) {
            alert("invalid accno")
        }
    }

    static withdrawal() {
        let dataset = Bank.accountDetails()
        var accno = document.querySelector("#accno").value
        var password = document.querySelector("#pwd").value
        var amount = document.querySelector("#amount").value
        let user = Bank.authenticate(accno, password)
        
        if (user == 0) {
            alert("invalid password")

        }
        else if (user == 1) {
            if (amount<dataset[accno]["balance"]) {
                alert("insufficient balance")
                
                
            }
            else {
                alert("amount successfully debited")
            }
        }
        else if (user == -1) {
            alert("invalid accno")
        }
    }

    static deposit() {
        let dataset = Bank.accountDetails()
        var accno = document.querySelector("#accno").value
        var password = document.querySelector("#pwd").value
        var amount = document.querySelector("#amount").value
        let user = Bank.authenticate(accno, password)
        if (user == 0) {
            alert("invalid password")
        }

        else if (user == 1) {
            if (amount < dataset[accno]["balance"]) {
                alert("no balance")
               
            }
            else {
                alert("amount successfully deposited")
            }
        }
        else if (user == -1) {
            alert("invalid accno")
        }
    }

}