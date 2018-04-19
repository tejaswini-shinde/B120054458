package com.example.tejaswini.calculator;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;


public class MainActivity extends AppCompatActivity
{
    TextView resultBox,ans;
    List<String> history;
    double num1;
    String op1;
    Button badd, bsub, bmul, bdiv, btan, bsin, bcos, beq, bclr, bsqrt, pr, nxt, his;
    int current;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        resultBox = findViewById(R.id.resultBox);
        ans=findViewById(R.id.ansBox);
        badd=findViewById(R.id.plus);
        bsub=findViewById(R.id.minus);
        bmul=findViewById(R.id.mul);
        bdiv=findViewById(R.id.div);
        bsin=findViewById(R.id.sin);
        bcos=findViewById(R.id.cos);
        btan=findViewById(R.id.tan);
        beq=findViewById(R.id.equal);
        bclr=findViewById(R.id.clear);
        bsqrt=findViewById(R.id.sqrt);
        pr=findViewById(R.id.prev);
        nxt=findViewById(R.id.next);
        his=findViewById(R.id.hist);
        history = new ArrayList<String>();

    }

    public void numberPressed(View v)
    {
        Button num = (Button) v;
        Log.i("meratag",resultBox.getText().toString()+num.getText().toString() );
        resultBox.setText(resultBox.getText().toString()+num.getText().toString());
    }

    public void opip(View v)
    {
        Button oper = (Button) v;
        op1 = oper.getText().toString();
        num1=Double.parseDouble(resultBox.getText().toString());
        resultBox.setText("");
    }

    public void result(View v)
    {
        Double res;
        String h1;
        switch(op1)
        {
            case "+":
                res = num1 + Double.parseDouble(resultBox.getText().toString());
                ans.setText(res.toString());
                h1 = num1+"+"+resultBox.getText().toString();
                history.add(h1);
                break;
            case "-":
                res = num1 - Double.parseDouble(resultBox.getText().toString());
                ans.setText(res.toString());
                h1 = num1+"-"+resultBox.getText().toString();
                history.add(h1);
                break;
            case "*":
                res = num1 * Double.parseDouble(resultBox.getText().toString());
                ans.setText(res.toString());
                h1 = num1+"*"+resultBox.getText().toString();
                history.add(h1);
                break;
            case "/":
                res = num1 / Double.parseDouble(resultBox.getText().toString());
                ans.setText(res.toString());
                h1 = num1+"/"+resultBox.getText().toString();
                history.add(h1);
                break;
            case "sqrt":
                res = Math.sqrt(num1);
                ans.setText(res.toString());
                h1 = "SQRT("+num1+")";
                history.add(h1);
                break;
            case "sin":
                res = Math.sin(Math.toRadians(num1));
                ans.setText(res.toString());
                h1 = "SIN("+num1+")";
                history.add(h1);
                break;
            case "cos":
                res = Math.cos(Math.toRadians(num1));
                ans.setText(res.toString());
                h1 = "COS("+num1+")";
                history.add(h1);
                break;
            case "tan":
                res = Math.tan(Math.toRadians(num1));
                ans.setText(res.toString());
                h1 = "TAN("+num1+")";
                history.add(h1);
                break;
        }

        resultBox.setText("");
    }

    public void clear(View v)
    {
        resultBox.setText("");
        ans.setText("");
    }

    public void memory(View v)
    {
        current = history.size()-1;
        if (current<0||current>history.size())
        {
            ans.setText("Out of Bound");
        }

        else
        {
            String disp = history.get(current);
            ans.setText(disp);
        }
    }

    public void prev(View v)
    {
        current--;
        String disp = history.get(current);
        ans.setText(disp);
    }

    public void next(View v)
    {
        current++;
        String disp = history.get(current);
        ans.setText(disp);
    }
}