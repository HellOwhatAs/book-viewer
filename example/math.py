[
    # MathJax support
    {
        "tag": "script",
        "innerText": r'''MathJax = {
            tex: {
                inlineMath: [['$', '$']]
            }, 
            startup: {
                typeset: false
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
        "echarts",
        [
            "<div id='main' style='width: 100%;height:50vh;'></div>"
        ],
        r"""
        var echarts_main = echarts.init(
            document.getElementById('main'),
            null, 
            {renderer: 'svg'}
        );
        echarts_main.setOption(
            {
                title: {text: 'ECharts Example'},
                tooltip: {},
                legend: {
                    data: ['Sales']
                },
                xAxis: {
                    data: ['shirt', 'cardigan', 'chiffon shirt', 'pants', 'high heels', 'socks']
                },
                yAxis: {},
                series: [
                    {
                        name: 'sales',
                        type: 'bar',
                        data: [5, 20, 36, 10, 10, 20]
                    }
                ]
            }
        );
        """
    ],
    "MathJax.typeset()"
]