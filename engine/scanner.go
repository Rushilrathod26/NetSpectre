package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

type PortInfo struct {
	Port    int    `json:"port"`
	Service string `json:"service"`
}

type ScanResult struct {
	Target    string     `json:"target"`
	OpenPorts []PortInfo `json:"open_ports"`
	ScanTime  float64    `json:"scan_time"`
}

func worker(target string, jobs <-chan int, results chan<- PortInfo, wg *sync.WaitGroup) {
	defer wg.Done()

	for port := range jobs {
		address := fmt.Sprintf("%s:%d", target, port)

		conn, err := net.DialTimeout("tcp", address, 500*time.Millisecond)

		if err == nil {
			conn.Close()
			service := ""

			switch port {
			case 22:
				service = "ssh"
			case 80:
				service = "http"
			case 443:
				service = "https"
			default:
				service = "unknown"
			}

			results <- PortInfo{
				Port:    port,
				Service: service,
			}
		}
	}
}

func main() {

	target := flag.String("target", "", "Target")
	ports := flag.String("ports", "1-1000", "Port Range")

	flag.Parse()

	if *target == "" {
		fmt.Println("Target required")
		return
	}

	rangeSplit := strings.Split(*ports, "-")

	start, _ := strconv.Atoi(rangeSplit[0])
	end, _ := strconv.Atoi(rangeSplit[1])

	startTime := time.Now()

	jobs := make(chan int, 100)
	results := make(chan PortInfo, 100)

	var wg sync.WaitGroup

	for i := 0; i < 200; i++ {
		wg.Add(1)
		go worker(*target, jobs, results, &wg)
	}

	go func() {
		for p := start; p <= end; p++ {
			jobs <- p
		}
		close(jobs)
	}()

	go func() {
		wg.Wait()
		close(results)
	}()

	var open []PortInfo

	for port := range results {
		open = append(open, port)
	}

	output := ScanResult{
		Target:    *target,
		OpenPorts: open,
		ScanTime:  time.Since(startTime).Seconds(),
	}

	json.NewEncoder(os.Stdout).Encode(output)
}
