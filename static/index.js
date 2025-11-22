 const form = document.getElementById("form");

        form.addEventListener("submit", async (e) => {
            e.preventDefault();

            const url = document.getElementById("url").value;

            const response = await fetch("/", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `url=${encodeURIComponent(url)}`
            });

            const data = await response.json();

            document.getElementById("short-url").textContent = data.url;
            document.getElementById("result").style.display = "block";
        });

        function copyURL() {
            const shortURL = document.getElementById("short-url").textContent;
            navigator.clipboard.writeText(shortURL);
            alert("Copied: " + shortURL);
        }