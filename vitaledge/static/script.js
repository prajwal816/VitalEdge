function checkFirstAid() {
    let problem = document.getElementById("problem").value;

    fetch("/first_aid", {
        method: "POST",
        body: new URLSearchParams({ problem: problem }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Advice: " + data.action;
    });
}

function logout() {
    window.location.href = "/logout";
}
