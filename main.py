import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

async def main():
    # Configure a 2-level deep crawl
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=2,  # Crawl initial page + 2 levels deep
            include_external=False,  # Stay within the same domain
            max_pages=50,  # Maximum number of pages to crawl (optional)
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun(
            url="https://www.qualityconnections.vip/",
            config=config
        )
        print(f"Crawled {len(results)} pages in total")

        # Access individual results
        for result in results:
            print(f"ЖЖЖЖ\n URL: {result.url}\n")
            print(f"ЖЖЖЖ\n Text: {result.markdown}\n")

if __name__ == "__main__":
    asyncio.run(main())