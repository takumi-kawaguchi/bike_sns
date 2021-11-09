package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/PuerkitoBio/goquery"
)

func main() {
	url := ""

	res, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()
	if res.StatusCode != http.StatusOK {
		log.Fatalf("status code: %d", res.StatusCode)
	}

	fmt.Println("request done")

	doc, err := goquery.NewDocumentFromReader(res.Body)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("parse doc")

	doc.Find("a.bikemaker-name").Each(func(i int, s *goquery.Selection) {
		name := s.Text()
		fmt.Println(name)
	})
}
