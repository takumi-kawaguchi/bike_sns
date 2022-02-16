package main

import (
	"path/filepath"

	"github.com/gin-contrib/multitemplate"
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.HTMLRender = loadTemplates("./templates")
	router.GET("/timeline", func(c *gin.Context) {
		c.HTML(200, "timeline.html", gin.H{
			"title": "タイムライン",
		})
	})
	router.GET("/post", func(c *gin.Context) {
		c.HTML(200, "post.html", gin.H{
			"title": "投稿画面",
		})
	})
	router.GET("/post/detail/:id", func(c *gin.Context) {
		c.HTML(200, "post_detail.html", gin.H{
			"title": "投稿詳細",
			"id":    c.Param("id"),
		})
	})
	router.GET("/search_bike", func(c *gin.Context) {
		c.HTML(200, "search_bike.html", gin.H{
			"title": "バイク検索",
		})
	})
	router.GET("/search_result", func(c *gin.Context) {
		c.HTML(200, "search_result.html", gin.H{
			"title": "検索結果",
		})
	})

	router.Run(":1323")
}

func loadTemplates(templatesDir string) multitemplate.Renderer {
	r := multitemplate.NewRenderer()

	layouts, err := filepath.Glob(templatesDir + "/layouts/*.html")
	if err != nil {
		panic(err.Error())
	}

	includes, err := filepath.Glob(templatesDir + "/includes/*.html")
	if err != nil {
		panic(err.Error())
	}

	// Generate our templates map from our layouts/ and includes/ directories
	for _, include := range includes {
		layoutCopy := make([]string, len(layouts))
		copy(layoutCopy, layouts)
		files := append(layoutCopy, include)
		test := filepath.Base(include)
		r.AddFromFiles(test, files...)
	}
	return r
}
