export default function AIAnalysis({

    analysis

}) {

    return (

        <div style={card}>

            <h2>
                AI Portfolio Analysis
            </h2>

            <p>
                Portfolio Strength:
                {analysis}
            </p>

        </div>
    );
}

const card = {

    background:"#172554",
    color:"white",
    padding:"20px",
    borderRadius:"20px",
    margin:"20px"
}