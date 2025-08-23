
package main

import (
    "bufio"
    "fmt"
    "net/http"
    "os"
    "strings"
    "sync"
)

// Warna terminal
const (
    Red    = "\033[31m"
    Green  = "\033[32m"
    Yellow = "\033[33m"
    Blue   = "\033[34m"
    Cyan   = "\033[36m"
    Reset  = "\033[0m"
)

func main() {
    // Header ASCII 
    fmt.Println(Cyan + `
















Peju3ncer - Hidden Finder
` + Reset)

    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Masukkan URL target: ")
    target, _ := reader.ReadString('\n')
    target = strings.TrimSpace(target)

    // Wordlist lebih panjang & lengkap
    wordlist := []string{
        "wp-sitemap.xml", "robots.txt", "sitemap.xml",
        "admin.php", "login.php", "wp-login.php",
        "wp-admin/", "config.php", "readme.html",
        ".env", "backup.zip", "backup.tar.gz",
        "uploads/", "uploads/images/", "test.php",
        "index_old.php", "old/", "dev/", "hidden/",
        "private/", "secret/", "db.sql", "database.sql",
        "administrator/", "controlpanel/", "user/", "users/",
        "tmp/", "temp/", "cache/", "logs/", "debug.php",
        "phpinfo.php", "info.php", "install.php", "setup.php",
        "wp-config.php", "wp-content/", "wp-includes/",
        ".git/", ".git/config", ".htaccess", ".htpasswd",
        "vendor/", "composer.json", "composer.lock",
        "backup/", "backup1/", "backup2/", "old_site/",
        "cms/", "site/", "data/", "files/", "documents/",
        "uploads/documents/", "uploads/files/", "media/", "images/",
        "includes/", "inc/", "core/", "system/", "lib/", "library/",
        "themes/", "plugins/", "modules/", "ext/", "extensions/",
        "admin/", "administrator/", "cpanel/", "panel/", "dashboard/",
        "webadmin/", "webmaster/", "test/", "demo/", "staging/",
        "development/", "devsite/", "beta/", "sandbox/", "tmp/", "temp/",
    }

    fmt.Println(Blue + "\nMencari link tersembunyi...\n" + Reset)

    var wg sync.WaitGroup
    sem := make(chan struct{}, 20) // max 20 concurrent requests
    
        for _, path := range wordlist {
        wg.Add(1)
        sem <- struct{}{} // acquire semaphore
        go func(p string) {
            defer wg.Done()
            url := target + "/" + p
            resp, err := http.Get(url)
            if err != nil {
                fmt.Printf(Red+"[Error]  %s\n"+Reset, url)
                <-sem
                return
            }
            resp.Body.Close()

            switch resp.StatusCode {
            case 200:
                fmt.Printf(Green+"[Found]  %s (Status: %d)\n"+Reset, url, resp.StatusCode)
            case 301, 302:
                fmt.Printf(Yellow+"[Redirect]  %s (Status: %d)\n"+Reset, url, resp.StatusCode)
            default:
                fmt.Printf(Blue+"[Not Found]  %s (Status: %d)\n"+Reset, url, resp.StatusCode)
            }
            <-sem // release semaphore
        }(path)
    }

    wg.Wait()
    fmt.Println(Cyan + "\n Pencarian selesai! " + Reset)
}