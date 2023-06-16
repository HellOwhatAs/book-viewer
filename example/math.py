BOOK = [
    # MathJax support
    {
        "tag": "script",
        "innerText": r'''MathJax = {
            tex: {
                inlineMath: [['$', '$']]
            }, 
            startup: {
                typeset: false
            },
            options: {
                enableMenu: false
            }
        };'''
    },
    {
        "tag": "script",
        "src": "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"
    },
    # pseudocode.js support
    {
        "tag": "link",
        "rel": "stylesheet",
        "href": "https://cdn.jsdelivr.net/npm/pseudocode@latest/build/pseudocode.min.css"
    },
    {
        "tag": "style",
        "innerText": r"""
            .ps-algorithm {
                border-top: 2px solid var(--color-font) !important;
                border-bottom: 2px solid var(--color-font) !important;
            }
            .ps-algorithm.with-caption > .ps-line {
                border-bottom: 2px solid var(--color-font) !important;
            }
        """
    },
    {
        "tag":"script",
        "src": "https://cdn.jsdelivr.net/npm/pseudocode@latest/build/pseudocode.min.js"
    },
    # echarts support
    {
        "tag": "script",
        "src": "https://cdn.jsdelivr.net/npm/echarts@5.4.2/dist/echarts.min.js"
    },
    [
        "MathJax",
        [
            r"Discriminative Model: $\frac{\partial}{\partial\theta}\log p(y|X)$",
            r"$$Z(\theta)=\sum\limits_{k}\exp\left(f_\theta^{(k)}(X)\right)$$",
            r"$$p(y|X)=\frac{\exp(f_\theta^{(k)}(X))}{Z(\theta)}$$",
            r"""$$\begin{aligned}
                \frac{\partial}{\partial\theta}\log p(y|X) &= \frac{\partial}{\partial\theta}\left(f_\theta^{(k)}(X) - \log\left(Z(\theta)\right)\right)\\
                &= \frac{\partial}{\partial\theta}f_\theta^{(k)}(X) - \frac{1}{Z(\theta)}\frac{\partial}{\partial\theta}Z(\theta)\\
                &= \frac{\partial}{\partial\theta}f_\theta^{(k)}(X) - \frac{1}{Z(\theta)}\frac{\partial}{\partial\theta}\left(\sum\limits_{k}\exp\left(f_\theta^{(k)}(X)\right)\right)\\
                &= \frac{\partial}{\partial\theta}f_\theta^{(k)}(X) - \sum\limits_{k'}\frac{1}{Z(\theta)}\frac{\partial}{\partial\theta}\exp\left(f_\theta^{(k')}(X)\right)\\
                &= \frac{\partial}{\partial\theta}f_\theta^{(k)}(X) - \sum\limits_{k'}\frac{\exp\left(f_\theta^{(k')}(X)\right)}{Z(\theta)}\frac{\partial}{\partial\theta}f_\theta^{(k')}(X)\\
                &= \frac{\partial}{\partial\theta}f_\theta^{(k)}(X) - \sum\limits_{k'}p_{k'}\frac{\partial}{\partial\theta}f_\theta^{(k')}(X)\\
                &= \sum\limits_{k'}\left(1(k=k')-p_{k'}\right)\frac{\partial}{\partial\theta}f_\theta^{(k')}(X)\\
                &= \frac{\partial}{\partial\theta}f_\theta(X)^\top(Y-p)\\
                &= \frac{\partial}{\partial\theta}f_\theta(X)^\top(Y-\text{E}_\theta(Y|X))
            \end{aligned}$$"""
        ]
    ],
    [
        "pseudocode.js",
        [
            r"""
            <pre id="alg1">
                % This quicksort algorithm is extracted from Chapter 7, Introduction to Algorithms (3rd edition)
                \begin{algorithm}
                \caption{Quicksort}
                \begin{algorithmic}
                \PROCEDURE{Quicksort}{$A, p, r$}
                    \IF{$p < r$} 
                        \STATE $q = $ \CALL{Partition}{$A, p, r$}
                        \STATE \CALL{Quicksort}{$A, p, q - 1$}
                        \STATE \CALL{Quicksort}{$A, q + 1, r$}
                    \ENDIF
                \ENDPROCEDURE
                \PROCEDURE{Partition}{$A, p, r$}
                    \STATE $x = A[r]$
                    \STATE $i = p - 1$
                    \FOR{$j = p$ \TO $r - 1$}
                        \IF{$A[j] < x$}
                            \STATE $i = i + 1$
                            \STATE exchange
                            $A[i]$ with $A[j]$
                        \ENDIF
                        \STATE exchange $A[i]$ with $A[r]$
                    \ENDFOR
                \ENDPROCEDURE
                \end{algorithmic}
                \end{algorithm}
            </pre>""",
            r"""
            <pre id="alg2">
                % This quicksort algorithm is extracted from Chapter 7, Introduction to Algorithms (3rd edition)
                \begin{algorithm}
                \caption{Quicksort}
                \begin{algorithmic}
                \PROCEDURE{Quicksort}{$A, p, r$}
                    \IF{$p < r$} 
                        \STATE $q = $ \CALL{Partition}{$A, p, r$}
                        \STATE \CALL{Quicksort}{$A, p, q - 1$}
                        \STATE \CALL{Quicksort}{$A, q + 1, r$}
                    \ENDIF
                \ENDPROCEDURE
                \PROCEDURE{Partition}{$A, p, r$}
                    \STATE $x = A[r]$
                    \STATE $i = p - 1$
                    \FOR{$j = p$ \TO $r - 1$}
                        \IF{$A[j] < x$}
                            \STATE $i = i + 1$
                            \STATE exchange
                            $A[i]$ with $A[j]$
                        \ENDIF
                        \STATE exchange $A[i]$ with $A[r]$
                    \ENDFOR
                \ENDPROCEDURE
                \end{algorithmic}
                \end{algorithm}
            </pre>"""
        ],
        'pseudocode.renderElement(document.getElementById("alg1"), { captionCount: 0});',
        'pseudocode.renderElement(document.getElementById("alg2"), { captionCount: 1});'
    ],
    [
        "<img src='https://echarts.apache.org/zh/images/favicon.png' style='height: 0.8em;'></img> echarts",
        [
            r"$$50\sin(x)\cos(2x+1)\sin(3x+2)$$"
            "<div id='main' style='width: 100%;height:90vh;'></div>"
        ],
        r"""
        var chartDom = document.getElementById('main');
        var myChart = echarts.init(chartDom, null, {renderer: 'svg'});
        var option;

        function func(x) {
            x /= 10;
            return Math.sin(x) * Math.cos(x * 2 + 1) * Math.sin(x * 3 + 2) * 50;
        }
        function generateData() {
            let data = [];
            for (let i = -100; i <= 100; i += 0.1) {
                data.push([i, func(i)]);
            }
            return data;
        }
        option = {
            animation: false,
            grid: {
                top: 40,
                left: 50,
                right: 40,
                bottom: 50
            },
            xAxis: {
                name: 'x',
                min: -100,
                max: 100,
                minorTick: {
                    show: true
                    },
                minorSplitLine: {
                    show: true
                    }
            },
            yAxis: {
                name: 'y',
                min: -100,
                max: 100,
                minorTick: {
                    show: true
                    },
                minorSplitLine: {
                    show: true
                    }
            },
            dataZoom: [
                {
                    show: true,
                    type: 'inside',
                    filterMode: 'none',
                    xAxisIndex: [0],
                    startValue: -20,
                    endValue: 20
                },
                {
                    show: true,
                    type: 'inside',
                    filterMode: 'none',
                    yAxisIndex: [0],
                    startValue: -20,
                    endValue: 20
                }
            ],
            series: [
                {
                    type: 'line',
                    showSymbol: false,
                    clip: true,
                    data: generateData()
                }
            ]
        };

        option && myChart.setOption(option);
        """
    ],
    "MathJax.typeset()"
]