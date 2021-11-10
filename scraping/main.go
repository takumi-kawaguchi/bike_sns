package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/PuerkitoBio/goquery"
)

func main() {
	bikeMaster := [][]string{
		// {"1", "ホンダ", "HONDA"},
		// {"2", "ヤマハ", "YAMAHA"},
		// {"3", "スズキ", "SUZUKI"},
		// {"4", "カワサキ", "KAWASAKI"},
		// {"5", "ハーレーダビッドソン", "Harley-Davidson"},
		// {"7", "ビーエムダブリュー", "BMW"},
		// {"8", "ドゥカティ", "DUCATI"},
		{"10", "トライアンフ", "TRIUMPH"},
		{"33", "ケーティーエム", "KTM"},
	}

	file, err := os.Create("bikeMaster.csv")
	if err != nil {
		log.Fatal(err)
	}

	w := csv.NewWriter(file)
	defer w.Flush()

	colHeader := []string{"id", "makerName", "englishMakerName", "bikeName"}
	w.Write(colHeader)

	for _, v := range bikeMaster {
		url := "https://www.bikebros.co.jp/catalog/" + v[0] + "/"
		res, err := http.Get(url)
		if err != nil {
			log.Fatal(err)
		}
		defer res.Body.Close()
		if res.StatusCode != http.StatusOK {
			log.Fatalf("status code: %d", res.StatusCode)
		}

		doc, err := goquery.NewDocumentFromReader(res.Body)
		if err != nil {
			log.Fatal(err)
		}

		doc.Find("a.bikemaker-name").Each(func(i int, s *goquery.Selection) {
			bikeName := s.Text()
			col := []string{v[0], v[1], v[2], bikeName}
			w.Write(col)
		})
		time.Sleep(time.Second * 1)
		fmt.Printf("finish: %s\n", v[2])
	}
}
